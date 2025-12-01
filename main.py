import math


def input_data():
    """Ввод всех исходных данных с консоли."""
    print("=== Ввод исходных данных ===")
    Qsut = float(input("Суточная выработка продукции Qсут (т): "))
    t = float(input("Продолжительность смены t (ч): "))
    at = float(input("Массовая доля теста аt (%): "))

    ppa = float(input("Производительность пельменного автомата pпа (т/ч): "))
    ptm = float(input("Производительность тестомесильной машины pтм (т/ч): "))
    pk = float(input("Производительность куттера pk (т/ч): "))

    return {
        "Qsut": Qsut,
        "t": t,
        "at": at,
        "ppa": ppa,
        "ptm": ptm,
        "pk": pk
    }


def calc_performance(data):
    """Расчёт производительности линий."""
    Qsut = data["Qsut"]
    t = data["t"]
    at = data["at"]

    # Производительность линии изготовления пельменей
    Ptl_p = Qsut / (2 * t)

    # Производительность линии приготовления теста
    Ptl_t = at * Ptl_p / 100

    # Производительность линии приготовления фарша
    Ptl_f = (100 - at) * Ptl_p / 100

    return Ptl_p, Ptl_t, Ptl_f


def calc_machines(Ptl_p, Ptl_t, Ptl_f, data):
    """Расчёт количества машин."""
    n_pa = math.ceil(Ptl_p / data["ppa"])    # пельменные автоматы
    n_tm = math.ceil(Ptl_t / data["ptm"])    # тестомесильные машины
    n_k = math.ceil(Ptl_f / data["pk"])      # куттеры

    return n_pa, n_tm, n_k


def output_results(n_pa, n_tm, n_k):
    """Вывод результатов."""
    print("\n=== Результаты расчёта ===")
    print(f"Пельменные автоматы (nпа): {n_pa}")
    print(f"Тестомесильные машины (nтм): {n_tm}")
    print(f"Куттеры (nк): {n_k}")


def main():
    data = input_data()
    Ptl_p, Ptl_t, Ptl_f = calc_performance(data)
    n_pa, n_tm, n_k = calc_machines(Ptl_p, Ptl_t, Ptl_f, data)
    output_results(n_pa, n_tm, n_k)


if __name__ == "__main__":
    main()
