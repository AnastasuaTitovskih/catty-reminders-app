"""
Простой модуль для демонстрации работы с Redis
"""
import redis
import os
import json

def get_redis_connection():
    """Создает подключение к Redis"""
    return redis.Redis(
        host=os.getenv('REDIS_HOST', 'redis'),
        port=int(os.getenv('REDIS_PORT', 6379)),
        decode_responses=True
    )

def cache_user_session(user_id, session_data):
    """Кеширует сессию пользователя"""
    r = get_redis_connection()
    key = f"session:{user_id}"
    r.setex(key, 3600, json.dumps(session_data))  # TTL 1 час
    return True

def get_user_session(user_id):
    """Получает сессию пользователя из кеша"""
    r = get_redis_connection()
    key = f"session:{user_id}"
    data = r.get(key)
    return json.loads(data) if data else None
