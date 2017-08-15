import fresh_tomatoes
import media

# This is our entertainment_center.py file.

# In this file we store all the movie parameters such as title, storyline, movie poster, and trailer. # noqa
transformers = media.movie("transformers",
                            "Humans are at war with the Transformers, and Optimus Prime is gone. The key to saving the future lies buried in the secrets of the past and the hidden history of Transformers on Earth. Now, it's up to the unlikely alliance of inventor Cade Yeager, Bumblebee, an English lord and an Oxford professor to save the world.",  # noqa
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQfKnoR3RsDT6gq3eEHzvH4XCt0Fal6sHiMZ7M98eyTF3ahSAPJ",  # noqa
                            "https://www.youtube.com/watch?v=Ue7cNNfjCyc")
troy = media.movie("troy",
                    "This epic portrays the battle between the ancient kingdoms of Troy and Sparta. While visiting Spartan King Menelaus (Brendan Gleeson), Trojan prince Paris (Orlando Bloom) falls for Menelaus' wife, Helen (Diane Kruger), and takes her back to Troy. Menelaus' brother, King Agamemnon (Brian Cox), having already defeated every army in Greece, uses his brother's fury as a pretext to declare war against Troy, the last kingdom preventing his control over the Aegean Sea.",  # noqa
                    "http://www.gstatic.com/tv/thumb/movieposters/34313/p34313_p_v8_aa.jpg",  # noqa
                    "https://www.youtube.com/watch?v=QpikTTSOHXc")
justice_league = media.movie("justice league",
                              "Fueled by his restored faith in humanity and inspired by Superman's (Henry Cavill) selfless act, Bruce Wayne (Ben Affleck) enlists newfound ally Diana Prince to face an even greater threat. Together, Batman and Wonder Woman work quickly to recruit a team to stand against this newly awakened enemy. Despite the formation of an unprecedented league of heroes -- Batman, Wonder Woman, Aquaman, Cyborg and the Flash -- it may be too late to save the planet from an assault of catastrophic proportions.",  # noqa
                              "http://t2.gstatic.com/images?q=tbn:ANd9GcQl4jDmsaajCfFvMRLWm7-3-lsXaJ4jc5BsJcpNZi1FypJUFuwE",  # noqa
                              "https://www.youtube.com/watch?v=TY078G4-tm8")
the_foreigner = media.movie("the foreigner",
                             "Quan is a humble London businessman whose long-buried past erupts in a revenge-fueled vendetta when the only person left for him to love -- his teenage daughter -- dies in a senseless act of politically motivated terrorism. His relentless search to find the terrorists leads to a cat-and-mouse conflict with a British government official whose own past may hold the clues to the identities of the elusive killers.",  # noqa
                             "http://t1.gstatic.com/images?q=tbn:ANd9GcTSL5uV_mSF9BIdlADGHdZteJcxVtfwO87bOwGAj1Ax5LTxT48M",  # noqa
                             "https://www.youtube.com/watch?v=LmImJ6ZUiqE")
black_panther = media.movie("black panther",
                             "Black Panther (Chadwick Boseman) springs into action when an old enemy threatens the fate of his nation and the world.",  # noqa
                             "http://t1.gstatic.com/images?q=tbn:ANd9GcS9XmH8C4x242GdYwyZtIOFOUqaZ5XMPSxY5zc2nVR_pbteQcSq",  # noqa
                             "https://www.youtube.com/watch?v=JBiZX_ceqO0")
bright = media.movie("bright",
                      "In an alternate present day, humans, orcs, elves and fairies have been coexisting since the beginning of time. Two police officers, one a human, the other an orc, embark on a routine night patrol that will alter the future of their world as they know it. Battling both their own personal differences as well as an onslaught of enemies, they must work together to protect a young female elf and a thought-to-be-forgotten relic, which, in the wrong hands, could destroy everything.",  # noqa
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5NTMyNTIxOV5BMl5BanBnXkFtZTgwMjM3NjU2MTI@._V1_UY1200_CR93,0,630,1200_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=giozR7nb51c")
movies = [transformers, troy, justice_league, the_foreigner, black_panther, bright]  # noqa
fresh_tomatoes.open_movies_page(movies)

