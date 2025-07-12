import matplotlib.pyplot as plt
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Построение диаграммы энергии уровней атома на основе данных из Excel-файла.")

parser.add_argument("orb_num", type=int, help="Количество орбиталей (например, 2 для s и p, 3 для s, p и d и т.д.).")
parser.add_argument("input_file_path", type=str, help="Путь к файлу с данными. Должен содержать столбец n с номерами уровней и столбцы с энергиями уровней " \
"для каждой орбитали.")
parser.add_argument("output_file_path", type=str, help="Путь к файлу, куда будет сохранена диаграмма.")

args = parser.parse_args()
if not args.output_file_path:
    raise ValueError("there's not enough arguments")

# Традиционные обозначения орбиталей
orbital_labels = ['s', 'p', 'd', 'f', 'g', 'h']
selected_orbitals = orbital_labels[:args.orb_num]
x_positions = {orb: i for i, orb in enumerate(selected_orbitals)}
width = 0.3

# === Загрузка данных из Excel ===
df = pd.read_excel(args.input_file_path)

# Проверка
assert 'n' in df.columns, "В таблице должен быть столбец 'n'"
assert len(df.columns) >= args.orb_num + 1, f"Ожидается минимум {args.orb_num + 1} столбцов (включая 'n')"

n_levels = df['n'].tolist()
energy_columns = df.columns[1:1 + args.orb_num]
energy_data = [df[col].tolist() for col in energy_columns]

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(6, 8))

# Рисуем уровни
for i, n in enumerate(n_levels):
    for j, orbital in enumerate(selected_orbitals):
        y = energy_data[j][i]
        ax.hlines(y=y, xmin=x_positions[orbital] - width, xmax=x_positions[orbital] + width,
                  color=f'C{j}', label=orbital if i == 0 else "")
        # Подпись справа
        ax.text(x_positions[orbital] + 0.35, y, f"n = {n}",
                      va='center', ha='left', fontsize=8, color=f'C{j}')

# Настройки осей
ax.set_xlim(-0.5, args.orb_num - 0.5)
ax.set_xticks([x_positions[o] for o in selected_orbitals])
ax.set_xticklabels(selected_orbitals)
ax.set_xlabel('Орбитальное квантовое число')
ax.set_ylabel('Энергия (эВ)')

# Cетка, заголовок
ax.grid(True, linestyle='--', alpha=0.5)
plt.title('Энергетические уровни электронов')

plt.tight_layout()
plt.savefig(args.output_file_path, dpi=300)