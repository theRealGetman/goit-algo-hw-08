import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів на мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад в купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
