input_message = """\
You are now an intelligent assistant tasked with meticulously extracting both key elements and \
atomic facts from a long text.
1. Key Elements: The essential nouns (e.g., characters, times, events, places, numbers), verbs (e.g., \
actions), and adjectives (e.g., states, feelings) that are pivotal to the text's narrative.
2. Atomic Facts: The smallest, indivisible facts, presented as concise sentences. These include \
propositions, theories, existences, concepts, and implicit elements like logic, causality, event \
sequences, interpersonal relationships, timelines, etc.
Requirements:
#####
1. Ensure that all identified key elements are reflected within the corresponding atomic facts.
2. You should extract key elements and atomic facts comprehensively, especially those that are \
important and potentially query-worthy and do not leave out details.
3. Whenever applicable, replace pronouns with their specific noun counterparts (e.g., change I, He, \
She to actual names).
4. Ensure that the key elements and atomic facts you extract are presented in the same language as \
the original text (e.g., English or Spanish).
"""