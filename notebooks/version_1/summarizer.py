# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="sshleifer/distilbart-cnn-12-6"
# )

# text = """The most defining shift in our defence story is the move from being a major importer
# to a global manufacturing hub. Under the vision of Atmanirbhar Bharat, India’s indigenous
# defence production reached an all-time high of ₹1.54 lakh crore in FY 2024–25.
# """

# print("Starting summarization...")
# result = summarizer(text, max_length=130, min_length=30, do_sample=False)
# print("Done.")
# print(result[0]["generated_text"])
