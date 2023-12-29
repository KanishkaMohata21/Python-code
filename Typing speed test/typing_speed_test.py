from tkinter import *
import time
import threading
import random
test_duration = 60
def check_speed():
    start.grid_forget()
    start_time = time.time()
    end_time = start_time + test_duration 

    original_paragraph = para_label.cget("text")
    user_input = text_entry.get()

    while time.time() < end_time:
        window.update()
        user_input = text_entry.get()

    elapsed_time = end_time - start_time
    typed_words = user_input.split()
    original_words = original_paragraph.split()

    correct_words = sum(1 for tw, ow in zip(typed_words, original_words) if tw == ow)
    accuracy = (correct_words / len(typed_words)) * 100 if len(original_words) > 0 else 0

    words_per_minute = int((len(typed_words) / elapsed_time) * 60)

    result_label.config(
        text=f"Time's up!\nYou typed {correct_words} correct words out of {len(original_words)} in {elapsed_time}sec.\nAccuracy: {accuracy:.2f}%\nYour typing speed: {words_per_minute} words per minute"
    )


BACKGROUND_COLOR = "#B1DDC6"
paragraphs = [
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet and is often used to test typing speed and accuracy.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The rapid advancement of technology is reshaping our world. From artificial intelligence to blockchain, these innovations are influencing every aspect of our lives.",
    "The sun dipped below the horizon, casting hues of orange and pink across the sky. The gentle rustle of leaves and the distant chirping of crickets created a symphony of nature's beauty.",
    "The moon landing on July 20, 1969, marked a significant achievement in human history. Astronaut Neil Armstrong's famous words, 'That's one small step for man, one giant leap for mankind,' echoed across the world.",
    "In a distant galaxy, a lone spaceship navigates through the cosmos, exploring uncharted planets and encountering extraterrestrial life forms. The crew's mission is to uncover the mysteries of the universe.",
    "Maintaining a healthy lifestyle involves a balance of regular exercise, nutritious meals, and adequate sleep. Small, consistent habits contribute to overall well-being.",
    "Backpacking through the picturesque landscapes of New Zealand, every turn reveals a breathtaking view. Majestic mountains, serene lakes, and lush greenery create an unforgettable travel experience.",
    "Shall I compare thee to a summer's day? Thou art more lovely and more temperate. Rough winds do shake the darling buds of May, and summer's lease hath all too short a date.",
    "The smell of freshly brewed coffee wafted through the air as people gathered in the cozy cafe. The hum of conversation and the clinking of cups created a warm and inviting atmosphere.",
    "In the heart of the bustling city, a hidden garden provided an oasis of tranquility. Lush foliage, colorful flowers, and the sound of a trickling fountain made it a secret retreat.",
    "As the raindrops danced on the windowsill, a feeling of coziness enveloped the room. The soft pitter-patter provided a soothing backdrop to a quiet evening indoors.",
    "The old bookstore was a treasure trove of literary gems. Dusty shelves held books with worn-out covers, each containing stories waiting to be discovered by eager readers.",
    "A solitary lighthouse stood tall against the crashing waves, guiding ships safely through the darkness. Its beacon symbolized hope and resilience in the face of adversity.",
    "Under the vast night sky, a campfire flickered, casting shadows on the faces of storytellers. Tales of adventure, mystery, and bravery captivated the audience gathered around.",
    "In the heart of the enchanted forest, mythical creatures roamed freely. Fairies flitted between flowers, and wise old owls observed the magical world with ancient wisdom.",
    "The melody of a piano echoed through the grand concert hall, captivating the audience. Each note was a masterpiece, creating a symphony that transcended time and space.",
    "As the first light of dawn painted the sky in hues of pink and gold, a new day unfolded. The world awakened to the promise of possibilities and fresh beginnings.",
    "In the serene meadow, butterflies danced among wildflowers, creating a kaleidoscope of colors. Nature's beauty was a canvas painted with the delicate strokes of creation.",
    "The ancient castle stood as a testament to bygone eras, its stone walls echoing the whispers of history. Time seemed to pause as visitors explored its hidden chambers.",
    "Beneath the starry night, a lone wolf howled, its mournful cry echoing through the wilderness. The moon cast a silvery glow, bathing the landscape in ethereal light.",
    "In the heart of the bustling market, vendors called out to passersby, showcasing vibrant fruits, spices, and handmade crafts. The air was filled with the aroma of exotic spices.",
    "Upon reaching the mountain's summit, the panoramic view took one's breath away. Rolling hills, distant valleys, and snow-capped peaks painted a picture of sublime beauty.",
    "A vintage typewriter sat on a weathered desk, its keys clicking rhythmically as a writer poured their thoughts onto paper. The room was filled with the creative energy of wordsmiths.",
    "In the coastal village, fishermen repaired their nets as seagulls circled overhead. The salty breeze carried tales of maritime adventures and the promise of fresh catches.",
    "As the first snowflake gently fell from the sky, a winter wonderland emerged. Trees adorned with frost sparkled in the sunlight, creating a magical scene.",
    "The aroma of freshly baked bread filled the neighborhood as the local bakery opened its doors. Warm loaves, crusty baguettes, and sweet pastries tempted the senses.",
    "Among the pages of an old journal, handwritten notes and pressed flowers told the story of a bygone romance. Each entry was a nostalgic journey through time.",
    "Beneath the twinkling city lights, couples strolled hand in hand along the riverbank. The reflection of skyscrapers shimmered on the water, creating a scene of urban romance.",
    "Amidst the rolling hills, a solitary windmill stood against the backdrop of a setting sun. Its blades turned gracefully, harnessing the power of the wind.",
    "The aroma of a home-cooked meal wafted from the kitchen, filling the house with warmth and comfort. Laughter and the clinking of utensils created a symphony of family moments.",
    "In the heart of the ancient forest, a wise old tree stood sentinel. Its gnarled branches and moss-covered trunk held the secrets of centuries gone by.",
    "A classic red telephone booth stood proudly on the cobblestone street, a nostalgic relic of a bygone era. Tourists posed for pictures, capturing a piece of history.",
    "Upon the canvas of the evening sky, the sun painted a masterpiece of colors. Shades of orange, pink, and purple blended harmoniously as day transitioned to night.",
    "On a lazy Sunday afternoon, the aroma of barbecue filled the air as families gathered in the backyard. The sizzle of grilling and joyous laughter created a festive atmosphere.",
    "A gentle breeze carried the sweet scent of blooming flowers in the botanical garden. Each blossom was a vibrant stroke in nature's ever-evolving masterpiece.",
    "In the heart of the bustling city, street performers showcased their talents. Music, dance, and art transformed the urban landscape into a vibrant celebration of creativity.",
    "The vintage train chugged along the tracks, carrying passengers on a nostalgic journey through picturesque landscapes. The rhythmic clatter echoed the romance of travel.",
    "As the full moon cast its silvery glow, nocturnal creatures emerged from the shadows. Owls hooted, and crickets played a nighttime symphony in the enchanted forest.",
    "The gentle lullaby of ocean waves provided a soothing soundtrack to a day at the beach. Seagulls soared overhead, and children built sandcastles in the warm sand.",
    "In the heart of the bustling market,the aroma of spices and the vibrant colors of exotic fruits created a sensory feast. Shopkeepers called out, inviting patrons to explore.",
    "On a rainy afternoon, the city streets glistened with reflections, and umbrellas formed a sea of colors. Puddles became mirrors, capturing the essence of urban life.",
    "As the city slept, the night sky became a canvas for the stars. Constellations told ancient stories, and the moon cast a soft glow over the silent streets.",
    "In the quiet library, the scent of old books mingled with the hushed whispers of readers. Each book held a world of knowledge waiting to be discovered.",
    "A field of sunflowers stretched endlessly, their golden faces following the sun's journey across the sky. The vibrant blooms created a sea of yellow and green.",
    "The bustling train station echoed with the sounds of arrivals and departures. Travelers hurriedly navigated the platforms, their journeys unfolding like chapters in a novel."
]

random_paragraph = random.choice(paragraphs)

window = Tk()
window.title("TYPING SPEED TEST")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

header = Label(text="Start typing... to test your speed", font="Arial,40,bold")
header.grid(row=0, column=1, pady=20)

para_label = Label(text=random_paragraph, wraplength=375, justify="left", font=("Arial", 12))
para_label.grid(row=1, column=0, columnspan=2)

text_entry = Entry(width=60)
text_entry.grid(row=2, column=1, columnspan=2, pady=20)


result_label = Label(text="Complete test to see result", font=("Arial", 12, "bold"), fg="blue")
result_label.grid(row=3, column=1, pady=20)

start=Button(text="START",command=check_speed)
start.grid(row=4,column=1)

window.mainloop()

