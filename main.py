import argparse
from finance_manager import FinanceManager


def main() -> None:
    parser = argparse.ArgumentParser(description="Sistema de finanzas personales")
    parser.add_argument("--archivo", default="finanzas.json", help="Archivo de datos")

    subparsers = parser.add_subparsers(dest="comando")

    p_ingreso = subparsers.add_parser("ingreso", help="Registrar un ingreso")
    p_ingreso.add_argument("monto", type=float)
    p_ingreso.add_argument("categoria")
    p_ingreso.add_argument("--descripcion", default="")

    p_gasto = subparsers.add_parser("gasto", help="Registrar un gasto")
    p_gasto.add_argument("monto", type=float)
    p_gasto.add_argument("categoria")
    p_gasto.add_argument("--descripcion", default="")

    subparsers.add_parser("balance", help="Mostrar balance actual")
    subparsers.add_parser("resumen", help="Mostrar resumen por categoria")

    args = parser.parse_args()
    fm = FinanceManager(args.archivo)

    if args.comando == "ingreso":
        fm.add_income(args.monto, args.categoria, args.descripcion)
    elif args.comando == "gasto":
        fm.add_expense(args.monto, args.categoria, args.descripcion)
    elif args.comando == "balance":
        print(f"Balance: {fm.balance():.2f}")
    elif args.comando == "resumen":
        for categoria, monto in fm.summary_by_category().items():
            print(f"{categoria}: {monto:.2f}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
