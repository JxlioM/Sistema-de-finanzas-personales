from finance_manager import FinanceManager


def test_income_and_expense(tmp_path):
    datafile = tmp_path / "finanzas.json"
    fm = FinanceManager(str(datafile))
    fm.add_income(1000, "salario")
    fm.add_expense(200, "comida")
    assert fm.balance() == 800
    resumen = fm.summary_by_category()
    assert resumen["salario"] == 1000
    assert resumen["comida"] == -200
    fm2 = FinanceManager(str(datafile))
    assert fm2.balance() == 800
