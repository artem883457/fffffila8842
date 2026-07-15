import asyncio
from models.base import init_db
from models.db_ops import add_car

async def populate():
    await init_db()
    
    cars = [
        ("BMW", "X5", "SUV", 2023, 8500000, "Отличное состояние, полная комплектация, один владелец."),
        ("Mercedes-Benz", "E-Class", "Седан", 2022, 6200000, "Комфортный седан бизнес-класса. Идеальное техническое состояние."),
        ("Toyota", "Camry", "Седан", 2021, 3500000, "Надежный японский автомобиль. Пробег 40,000 км."),
        ("Audi", "Q7", "SUV", 2023, 9200000, "Премиальный внедорожник. Панорамная крыша, кожаный салон."),
        ("Tesla", "Model 3", "Электро", 2022, 4800000, "Электромобиль в идеальном состоянии. Автопилот, большой запас хода.")
    ]
    
    for brand, model, cat, year, price, desc in cars:
        await add_car(brand, model, cat, year, price, desc)
    
    print("Database initialized and populated with sample data.")

if __name__ == "__main__":
    asyncio.run(populate())
