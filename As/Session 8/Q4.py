# 4.
# Given a Flipkart product description string, write a Python script that extracts and prints the first word, last word, and the total number of words using string methods split(), indexing, and len().



description = "Samsung Galaxy S24 Ultra Smartphone"

words = description.split()

print("First Word:", words[0])
print("Last Word:", words[-1])
print("Total Words:", len(words))