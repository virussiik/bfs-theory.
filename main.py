from collections import deque


def print_section(title, text):
    print(f"\n{title}")
    print("-" * len(title))
    print(text)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def shortest_path_bfs(graph, start, goal):
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        if vertex == goal:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def main():
    print_section(
        "1. Основи графів",
        "Граф складається з вершин і ребер. Вершини - це об'єкти, "
        "а ребра - зв'язки між ними. Шлях - це послідовність ребер, "
        "якою можна перейти від однієї вершини до іншої.",
    )

    print_section(
        "2. Представлення графів у пам'яті",
        "Найчастіше використовують список суміжності або матрицю суміжності. "
        "У цьому прикладі використано список суміжності, бо він зручний "
        "для зберігання сусідів кожної вершини.",
    )

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Список суміжності:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")

    print_section(
        "3. BFS: алгоритм і реалізація",
        "BFS працює за принципом черги: спочатку обробляються найближчі "
        "вершини, потім вершини наступного рівня. Це дозволяє знаходити "
        "найкоротший шлях у незваженому графі.",
    )

    start_vertex = "A"
    finish_vertex = "F"

    order = bfs(graph, start_vertex)
    path = shortest_path_bfs(graph, start_vertex, finish_vertex)

    print(f"Порядок обходу BFS від вершини {start_vertex}: {' -> '.join(order)}")

    if path:
        print(
            f"Найкоротший шлях від {start_vertex} до {finish_vertex}: "
            f"{' -> '.join(path)}"
        )
    else:
        print(f"Шлях від {start_vertex} до {finish_vertex} не знайдено.")

    print_section(
        "4. Приклади використання BFS у житті",
        "BFS використовують для пошуку маршруту в метро, аналізу соціальних "
        "мереж, обходу файлової системи, пошуку шляху в іграх і розв'язання "
        "головоломок з мінімальною кількістю ходів.",
    )


if __name__ == "__main__":
    main()
