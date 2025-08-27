# Sistema de Finanzas Personales

Aplicación simple escrita en Python para registrar ingresos y gastos, y obtener un balance y resumen por categoría.

## Uso

```bash
python main.py ingreso 1000 salario --descripcion "Pago mensual"
python main.py gasto 200 comida --descripcion "Cena"
python main.py balance
python main.py resumen
```

Los datos se guardan en `finanzas.json` en el directorio actual.

## Pruebas

Ejecuta las pruebas con:

```bash
pytest
```
