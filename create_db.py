from clickhouse_driver import Client

# Установка соединения с ClickHouse
client = Client('clickhouse')

# Создание БД starwars
client.execute('CREATE DATABASE IF NOT EXISTS starwars')

# Создание таблицы films_table
client.execute('''
    CREATE TABLE IF NOT EXISTS starwars.films_table (
        title String,
        episode_id Int32,
        opening_crawl String,
        director String,
        producer String,
        release_date Date,
        species Array(String),
        starships Array(String),
        vehicles Array(String),
        characters Array(String),
        planets Array(String),
        url String,
        created String,
        edited String
    ) ENGINE = MergeTree() ORDER BY title
''')

# Создание таблицы starships_table
client.execute('''
    CREATE TABLE IF NOT EXISTS starwars.starships_table (
        name String,
        model String,
        starship_class String,
        manufacturer String,
        cost_in_credits String,
        length String,
        crew String,
        passengers String,
        max_atmosphering_speed String,
        hyperdrive_rating String,
        MGLT String,
        cargo_capacity String,
        consumables String,
        films Array(String),
        pilots Array(String),
        url String,
        created String,
        edited String
    ) ENGINE = MergeTree() ORDER BY name
''')

# Создание таблицы vehicles_table
client.execute('''
    CREATE TABLE IF NOT EXISTS starwars.vehicles_table (
        name String,
        model String,
        vehicle_class String,
        manufacturer String,
        length String,
        cost_in_credits String,
        crew String,
        passengers String,
        max_atmosphering_speed String,
        cargo_capacity String,
        consumables String,
        films Array(String),
        pilots Array(String),
        url String,
        created String,
        edited String
    ) ENGINE = MergeTree() ORDER BY name
''')

# Создание таблицы species_table
client.execute('''
    CREATE TABLE IF NOT EXISTS starwars.species_table (
        name String,
        classification String,
        designation String,
        average_height String,
        average_lifespan String,
        eye_colors String,
        hair_colors String,
        skin_colors String,
        language String,
        homeworld String,
        people Array(String),
        films Array(String),
        url String,
        created String,
        edited String
    ) ENGINE = MergeTree() ORDER BY name
''')

# Создание таблицы planets_table
client.execute('''
    CREATE TABLE IF NOT EXISTS starwars.planets_table (
        name String,
        diameter String,
        rotation_period String,
        orbital_period String,
        gravity String,
        population String,
        climate String,
        terrain String,
        surface_water String,
        residents Array(String),
        films Array(String),
        url String,
        created String,
        edited String
    ) ENGINE = MergeTree() ORDER BY name
''')

# Создание таблицы people_table
client.execute('''
    CREATE TABLE IF NOT EXISTS starwars.people_table (
        name String,
        birth_year String,
        eye_color String,
        gender String,
        hair_color String,
        height String,
        mass String,
        skin_color String,
        homeworld String,
        films Array(String),
        species Array(String),
        starships Array(String),
        vehicles Array(String),
        url String,
        created String,
        edited String
    ) ENGINE = MergeTree() ORDER BY name
''')

print("Таблицы успешно созданы в базе данных 'starwars'")
