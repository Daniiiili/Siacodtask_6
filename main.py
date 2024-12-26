from collections import defaultdict

def topolog_sort(dependencies):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    graph = defaultdict(list)
    for lib, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(lib)

    visited = set()
    result = []
    for lib in dependencies.keys():
        if lib not in visited:
            dfs(lib)

    return result[::-1]

dependencies = {
    "Проект": ["Lib1", "Lib2", "Lib3"],
    "Lib1": ["Lib4"],
    "Lib2": ["Lib6", "Lib7"],
    "Lib3": [],
    "Lib4": ["Lib5", "Lib6"],
    "Lib5": [],
    "Lib6": [],
    "Lib7": []
}


order = topolog_sort(dependencies)
print("Порядок установки библиотек:", order)
