#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import fnmatch

def ids(root, target, max_depth):
    for depth in range(max_depth + 1):
        found_files = dls(root, target, depth)
        if found_files:
            return found_files
    return []

def dls(current_dir, target, depth):
    if depth == 0:
        return []
    
    found_files = []
    
    try:
        entries = os.listdir(current_dir)
    except PermissionError:
        return []

    for entry in entries:
        full_path = os.path.join(current_dir, entry)
        
        # Если это файл, проверяем его имя
        if os.path.isfile(full_path) and target in entry:
            found_files.append(full_path)
        
        # Если это директория, рекурсивно ищем в ней
        elif os.path.isdir(full_path):
            found_files.extend(dls(full_path, target, depth - 1))
    
    return found_files

if __name__ == "__main__":
    root_directory = input("Введите корневую директорию для поиска: ")
    search_term = "backup"
    max_search_depth = 5  # Задайте максимальную глубину поиска

    results = ids(root_directory, search_term, max_search_depth)

    if results:
        print("Найдены файлы:")
        for file in results:
            print(file)
    else:
        print("Файлы не найдены.")