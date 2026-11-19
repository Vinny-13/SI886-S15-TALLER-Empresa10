import pandas as pd

columns = ["id", "Valor", "Valor residual", "Decisión"]
t = pd.read_csv("RG04_tratamiento.csv", keep_default_na=False)
assert t.id.is_unique
assert (t["Valor residual"] == t["P residual"] * t["I residual"]).all()
t["Reducción"] = t.Valor - t["Valor residual"]
t["Reducción %"] = (100 * t["Reducción"] / t.Valor).round(1)
assert (t["Reducción"] >= 0).all()
print(t[columns + ["Reducción", "Reducción %"]].to_string(index=False))
original = t.Valor.sum()
residual = t["Valor residual"].sum()
print(f"\nValor inicial agregado: {original}")
print(f"Valor residual agregado: {residual}")
print(f"Reducción estimada: {original - residual} puntos ({(original - residual) / original:.1%})")
print("El agregado describe el cambio en la escala ordinal. No es una pérdida monetaria.")
over = t[t["Valor residual"] > 6]
print(f"\nResiduales > 6 con aceptación formal pendiente ({len(over)})")
print(over[["id", "Valor residual", "¿Quién acepta el residual?"]].to_string(index=False))
scope = t[t.Valor > 6]
empty = scope[scope["Señal temprana"].str.strip().eq("") | scope["Umbral de alerta"].str.strip().eq("")]
print(f"\nRiesgos > 6 sin señal o umbral: {len(empty)}")
assert empty.empty
