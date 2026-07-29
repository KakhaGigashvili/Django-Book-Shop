from django.db import migrations

def add_books(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    books = [
    {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "price": 14.99,
    "description": "Bilbo Baggins is a peaceful hobbit living a quiet life in the Shire until the wizard Gandalf arrives and invites him on an unexpected adventure. Together with thirteen dwarves, Bilbo travels across Middle-earth to reclaim the lost kingdom of Erebor from the dragon Smaug. During his journey, he discovers courage, friendship, and a hidden strength within himself.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg",
},
{
    "title": "1984",
    "author": "George Orwell",
    "price": 12.50,
    "description": "George Orwell's famous dystopian novel follows Winston Smith, a man living under the control of the Party and its leader Big Brother. In a world where surveillance, propaganda, and manipulation dominate everyday life, Winston begins questioning the reality he has always known. The book explores themes of freedom, truth, government control, and the dangers of absolute power.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg",
},
{
    "title": "Dune",
    "author": "Frank Herbert",
    "price": 16.99,
    "description": "Dune tells the story of Paul Atreides, whose family takes control of the desert planet Arrakis, the only source of the valuable spice melange. As political conflicts and dangerous enemies threaten his family, Paul discovers secrets about his destiny and the future of the universe. The novel combines science fiction, politics, philosophy, and adventure in an unforgettable epic.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780441172719-L.jpg",
},
{
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "price": 10.99,
    "description": "Through the eyes of young Scout Finch, this novel explores childhood, justice, and morality in a small American town. Her father Atticus Finch defends a man accused of a serious crime despite facing prejudice and social pressure. The story examines compassion, courage, and the importance of understanding others.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780061120084-L.jpg",
},
{
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "price": 9.99,
    "description": "Elizabeth Bennet is an intelligent and independent young woman navigating love, family expectations, and social traditions in 19th-century England. Her complicated relationship with the wealthy Mr. Darcy develops through misunderstandings, pride, and personal growth. Jane Austen's classic novel remains one of the greatest stories about love and human relationships.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg",
},
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 11.99,
    "description": "The novel follows Nick Carraway as he becomes fascinated by his mysterious millionaire neighbor Jay Gatsby and his extravagant lifestyle. Behind the wealth and parties lies Gatsby's dream of restoring a lost love. The story explores ambition, obsession, wealth, and the illusion of the American Dream.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780743273565-L.jpg",
},
{
    "title": "Fahrenheit 451",
    "author": "Ray Bradbury",
    "price": 13.50,
    "description": "In a future society where books are banned and firefighters burn them instead of stopping fires, Guy Montag begins questioning the world around him. His search for knowledge leads him to discover the importance of literature, independent thinking, and human connection. The novel explores censorship, technology, and the power of ideas.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9781451673319-L.jpg",
},
{
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "price": 10.50,
    "description": "Holden Caulfield tells the story of his experiences after leaving school and struggling with loneliness, identity, and the challenges of growing up. Through his unique perspective, the novel explores teenage emotions, confusion, and the search for meaning. Holden's journey has made this book one of the most recognized coming-of-age stories.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780316769488-L.jpg",
},
{
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "price": 12.99,
    "description": "Aldous Huxley's dystopian masterpiece presents a future society where technology and social engineering create an apparently perfect world. However, beneath the comfort and stability lies a loss of individuality, emotions, and freedom. The novel questions whether happiness without choice is truly happiness.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780060850524-L.jpg",
},
{
    "title": "Moby-Dick",
    "author": "Herman Melville",
    "price": 15.99,
    "description": "Ishmael joins the crew of the whaling ship Pequod under the command of the obsessed Captain Ahab. Ahab's only goal is to hunt down the legendary white whale Moby-Dick, which he believes is responsible for his suffering. The novel explores obsession, revenge, human nature, and humanity's relationship with the unknown.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780142437247-L.jpg",
},
{
    "title": "War and Peace",
    "author": "Leo Tolstoy",
    "price": 19.99,
    "description": "Leo Tolstoy's monumental novel follows several aristocratic families during the Napoleonic Wars and explores their personal struggles, relationships, and search for meaning. Through characters such as Pierre Bezukhov, Natasha Rostova, and Prince Andrei, the story examines love, ambition, war, peace, and the forces that shape human history.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9781400079988-L.jpg",
},
{
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevsky",
    "price": 14.50,
    "description": "The novel follows Rodion Raskolnikov, a poor former student who commits a terrible crime believing that some people are above ordinary moral rules. As guilt and psychological suffering consume him, he begins a journey toward understanding, redemption, and responsibility. Dostoevsky explores morality, human nature, and the consequences of one's choices.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780143058144-L.jpg",
},
{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "price": 24.99,
    "description": "The Lord of the Rings follows Frodo Baggins and the Fellowship as they attempt to destroy the One Ring before the Dark Lord Sauron can use it to conquer Middle-earth. Along their journey they face powerful enemies, difficult choices, and unimaginable dangers. The story is a timeless epic about friendship, courage, sacrifice, and the struggle between good and evil.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780618640157-L.jpg",
},
{
    "title": "Animal Farm",
    "author": "George Orwell",
    "price": 8.99,
    "description": "Animal Farm is a powerful political allegory about a group of farm animals who overthrow their human owner hoping to create a fair society. However, their new leaders slowly become as corrupt as the rulers they replaced. Orwell's story explores power, propaganda, inequality, and the dangers of totalitarianism.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780451526342-L.jpg",
},
{
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "price": 13.99,
    "description": "The Alchemist follows Santiago, a young shepherd who dreams of discovering a hidden treasure near the Egyptian pyramids. His journey introduces him to different people and lessons about destiny, courage, and following one's dreams. The novel is a philosophical story about finding purpose and listening to your heart.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780062315007-L.jpg",
},
{
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "price": 15.50,
    "description": "Harry Potter discovers that he is a wizard and begins his first year at Hogwarts School of Witchcraft and Wizardry. There he makes lifelong friendships, learns magic, and uncovers secrets about his mysterious past. The book introduces the magical world of Hogwarts and the beginning of Harry's battle against darkness.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780590353427-L.jpg",
},
{
    "title": "The Da Vinci Code",
    "author": "Dan Brown",
    "price": 12.99,
    "description": "The Da Vinci Code follows symbologist Robert Langdon as he investigates a mysterious murder connected to ancient secrets hidden throughout history. Alongside cryptologist Sophie Neveu, he follows a trail of clues involving art, religion, and secret organizations. The novel combines mystery, adventure, and historical conspiracy.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780307474278-L.jpg",
},
{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "price": 11.50,
    "description": "In the dystopian nation of Panem, Katniss Everdeen volunteers to participate in the deadly Hunger Games to protect her younger sister. Forced to fight for survival in a brutal televised competition, Katniss becomes a symbol of resistance against oppression. The novel explores courage, sacrifice, power, and rebellion.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780439023481-L.jpg",
},
{
    "title": "The Silmarillion",
    "author": "J.R.R. Tolkien",
    "price": 18.99,
    "description": "The Silmarillion tells the ancient history of Middle-earth, describing the creation of the world, the rise and fall of powerful kingdoms, and the great battles between good and evil. It introduces legendary figures such as Morgoth, Beren, Lúthien, and the ancestors of many characters from The Lord of the Rings. This book provides the mythology and deep history behind Tolkien's greatest fantasy world.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780618391110-L.jpg",
},
{
    "title": "The Children of Húrin",
    "author": "J.R.R. Tolkien",
    "price": 17.99,
    "description": "The Children of Húrin is a tragic tale set during the First Age of Middle-earth. It follows Túrin Turambar, a great warrior whose life is shaped by a terrible curse placed upon his family. The story explores destiny, pride, courage, and the devastating consequences of choices made during times of darkness.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780618894642-L.jpg",
},
{
    "title": "A Game of Thrones",
    "author": "George R.R. Martin",
    "price": 19.99,
    "description": "The first novel in A Song of Ice and Fire introduces the kingdoms of Westeros, where noble families compete for power and control of the Iron Throne. The story follows characters from House Stark, House Lannister, and other great families as they face political intrigue, war, betrayal, and ancient threats returning from the past.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780553593716-L.jpg",
},
{
    "title": "A Clash of Kings",
    "author": "George R.R. Martin",
    "price": 20.99,
    "description": "The struggle for the Iron Throne continues as several kings claim the right to rule Westeros. While armies clash across the realm, new alliances are formed and old friendships are tested. The novel expands the world with deeper politics, complex characters, and the growing threat beyond the Wall.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780553579901-L.jpg",
},
{
    "title": "A Storm of Swords",
    "author": "George R.R. Martin",
    "price": 22.99,
    "description": "A Storm of Swords is one of the most dramatic entries in the A Song of Ice and Fire series. As the War of the Five Kings reaches its peak, characters face unexpected betrayals, dangerous battles, and life-changing decisions. The novel is known for its shocking events, political complexity, and unforgettable moments.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780553573428-L.jpg",
},
{
    "title": "The Name of the Wind",
    "author": "Patrick Rothfuss",
    "price": 16.99,
    "description": "The Name of the Wind tells the story of Kvothe, a legendary figure who reveals the truth behind the myths surrounding his life. From his childhood to his years studying at a magical university, Kvothe's journey is filled with music, friendship, danger, and discovery. The novel is praised for its beautiful writing and detailed fantasy world.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780756404741-L.jpg",
},
{
    "title": "The Wise Man's Fear",
    "author": "Patrick Rothfuss",
    "price": 18.99,
    "description": "The Wise Man's Fear continues Kvothe's journey as he searches for knowledge, adventure, and the truth about the mysterious forces that changed his life. He explores new lands, learns ancient secrets, and faces challenges that test his skills and beliefs. The novel expands the world introduced in The Name of the Wind.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780756407919-L.jpg",
},
{
    "title": "Mistborn: The Final Empire",
    "author": "Brandon Sanderson",
    "price": 18.50,
    "description": "Mistborn: The Final Empire takes place in a world ruled by the immortal Lord Ruler, where the oppressed skaa people have suffered for centuries. A young thief named Vin discovers powerful abilities and joins a group planning an impossible rebellion. The story combines magic, political strategy, friendship, and an unforgettable fantasy adventure.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765311788-L.jpg",
},
{
    "title": "The Well of Ascension",
    "author": "Brandon Sanderson",
    "price": 18.99,
    "description": "The Well of Ascension follows Vin and her allies as they struggle to build a new society after overthrowing the Lord Ruler. Facing political enemies, powerful forces, and uncertainty about the future, they must discover what true leadership means. The novel expands the Mistborn world with deeper characters and greater conflicts.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765316882-L.jpg",
},
{
    "title": "The Hero of Ages",
    "author": "Brandon Sanderson",
    "price": 19.50,
    "description": "The Hero of Ages concludes the original Mistborn trilogy with an epic battle for the survival of the world. Vin and her companions uncover ancient secrets while facing a threat far greater than anything they imagined. The novel delivers a powerful conclusion filled with sacrifice, discovery, and unexpected revelations.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765316899-L.jpg",
},
{
    "title": "The Way of Kings",
    "author": "Brandon Sanderson",
    "price": 24.99,
    "description": "The Way of Kings is the first novel in The Stormlight Archive, an epic fantasy series set in the world of Roshar. The story follows Kaladin, a former soldier struggling with loss and purpose, and Dalinar Kholin, a nobleman searching for answers about ancient legends. Filled with powerful characters, complex politics, and a unique magic system, the novel explores honor, leadership, and the meaning of courage.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765326355-L.jpg",
},
{
    "title": "Words of Radiance",
    "author": "Brandon Sanderson",
    "price": 25.99,
    "description": "Words of Radiance continues the story of the Knights Radiant as new threats appear across Roshar. Kaladin struggles with his responsibilities and powers, while Shallan uncovers secrets hidden in the past. The novel expands the world with greater battles, deeper mysteries, and unforgettable moments of heroism.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765326362-L.jpg",
},
{
    "title": "Oathbringer",
    "author": "Brandon Sanderson",
    "price": 27.99,
    "description": "Oathbringer follows Dalinar Kholin as he attempts to unite the kingdoms of Roshar against an ancient enemy returning to destroy civilization. Haunted by memories of his violent past, Dalinar must discover whether a person can truly change. The book explores redemption, leadership, friendship, and the responsibilities of power.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765326379-L.jpg",
},
{
    "title": "Rhythm of War",
    "author": "Brandon Sanderson",
    "price": 29.99,
    "description": "Rhythm of War continues the epic conflict between the forces of humanity and their ancient enemies. The characters face new challenges as they search for discoveries that could change the future of Roshar. The novel combines large-scale battles with personal struggles, scientific exploration, and emotional character development.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780765326386-L.jpg",
},
{
    "title": "The Eye of the World",
    "author": "Robert Jordan",
    "price": 17.99,
    "description": "The Eye of the World begins The Wheel of Time series and introduces a world where ancient forces of darkness are returning. When young villagers from the peaceful Two Rivers are forced to leave their home, they begin a journey that will change the fate of the world. The novel combines adventure, magic, friendship, and a battle between light and darkness.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780812511819-L.jpg",
},
{
    "title": "The Lies of Locke Lamora",
    "author": "Scott Lynch",
    "price": 15.99,
    "description": "The Lies of Locke Lamora follows Locke Lamora, a brilliant thief and master of deception living in the dangerous city of Camorr. Along with his group of skilled criminals, Locke creates impossible schemes while trying to survive powerful enemies. The novel combines fantasy, clever storytelling, humor, and thrilling adventures.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780553588941-L.jpg",
},
{
    "title": "The Blade Itself",
    "author": "Joe Abercrombie",
    "price": 16.99,
    "description": "The Blade Itself introduces the dark fantasy world of The First Law series, where heroes are flawed and morality is complicated. The story follows characters including the ruthless warrior Logen Ninefingers, the tortured inquisitor Glokta, and the ambitious nobleman Jezal dan Luthar. The novel explores war, politics, survival, and the darker side of humanity.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780316387316-L.jpg",
},
{
    "title": "The Colour of Magic",
    "author": "Terry Pratchett",
    "price": 14.99,
    "description": "The Colour of Magic is the first novel in the Discworld series and introduces a unique fantasy world filled with humor and imagination. The story follows the inexperienced wizard Rincewind and the curious tourist Twoflower as they travel through dangerous and bizarre lands. Terry Pratchett combines comedy, fantasy, and clever social commentary in this classic adventure.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780062225672-L.jpg",
},
{
    "title": "Eragon",
    "author": "Christopher Paolini",
    "price": 14.99,
    "description": "Eragon follows a young farm boy who discovers a mysterious dragon egg that changes his life forever. After becoming a Dragon Rider, Eragon begins a dangerous journey filled with magic, battles, and ancient secrets. The novel tells a classic coming-of-age story about courage, destiny, and the fight against tyranny.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780375826696-L.jpg",
},
{
    "title": "The Chronicles of Narnia",
    "author": "C.S. Lewis",
    "price": 21.99,
    "description": "The Chronicles of Narnia is a collection of fantasy adventures set in the magical world of Narnia, where children discover a land filled with talking animals, powerful creatures, and legendary battles. The stories explore friendship, bravery, sacrifice, and the struggle between good and evil. It remains one of the most beloved fantasy series ever written.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780066238500-L.jpg",
},
{
    "title": "Dracula",
    "author": "Bram Stoker",
    "price": 11.99,
    "description": "Dracula tells the terrifying story of Count Dracula, a mysterious vampire from Transylvania who travels to England searching for new victims. Through letters, journals, and reports, the characters uncover the truth about the supernatural threat they face. The novel became one of the most influential works in gothic horror literature.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780141439846-L.jpg",
},
{
    "title": "Frankenstein",
    "author": "Mary Shelley",
    "price": 10.99,
    "description": "Frankenstein follows Victor Frankenstein, a young scientist who creates a living creature through an experiment that goes terribly wrong. The novel explores ambition, responsibility, loneliness, and the consequences of trying to control nature. Mary Shelley's masterpiece is considered one of the earliest and most important science fiction novels.",
    "image_url": "https://covers.openlibrary.org/b/isbn/9780141439471-L.jpg",
},
]
    for book_data in books:
        Book.objects.create(**book_data)

def remove_books(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    Book.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_books, remove_books),
    ]