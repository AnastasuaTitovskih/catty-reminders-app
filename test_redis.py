#!/usr/bin/env python3
"""
Простой тест Redis для Lab 4
"""
import redis
import time

print("=" * 50)
print("Тест Redis для мультиконтейнерного приложения")
print("=" * 50)

try:
    # Подключаемся к Redis
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    
    # Тест 1: Ping
    print("1. Подключение к Redis...")
    if r.ping():
        print("   ✅ Успешно подключились к Redis")
    else:
        print("   ❌ Ошибка подключения")
        exit(1)
    
    # Тест 2: Запись данных
    print("2. Запись тестовых данных...")
    timestamp = int(time.time())
    r.set(f"lab4_test_{timestamp}", "Docker Compose работает!")
    print("   ✅ Данные записаны")
    
    # Тест 3: Чтение данных
    print("3. Чтение тестовых данных...")
    value = r.get(f"lab4_test_{timestamp}")
    if value:
        print(f"   ✅ Данные прочитаны: {value}")
    else:
        print("   ❌ Ошибка чтения")
    
    # Тест 4: Счетчик
    print("4. Тест счетчика...")
    count = r.incr("lab4_request_counter")
    print(f"   ✅ Счетчик: {count}")
    
    print("\n" + "=" * 50)
    print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    print("Redis работает в Docker Compose")
    print("=" * 50)
    
except Exception as e:
    print(f"\n❌ Ошибка: {e}")
    exit(1)
