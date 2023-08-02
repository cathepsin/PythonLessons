map_of_codons = {
  "AAA" : "Z",
  "ABA" : "T",
  "BCA" : "U",
  "CAA" : "F"
}

mass_of_AA = {
  "Z" : 134.20,
  "T" : 97.52,
  "U" : 174.91,
  "F" : 156.48
}

def Translate(sequence):
  translated = ""
  for i in range(0, len(sequence), 3): #You don't need to do len() - 1 here because we are using i for list splicing, which protects against out-of-index searches
    if sequence[i: i+3] in map_of_codons.keys():
      translated += map_of_codons[ sequence[i: i+3] ]
    else:
      return "Invalid Sequence"
  return translated

def Weigh(sequence):
  weight = 0
  for c in sequence:
    weight += mass_of_AA[c]
  return weight

def TranslateAndWeigh(DNASequence):
  print(f"Received DNA sequence: {DNASequence}")
  translatedSequence = Translate(DNASequence)
  if translatedSequence == "Invalid Sequence":
    print(translatedSequence)
    return

  totalMass = Weigh(translatedSequence)

  print(f"Translated AA sequence: {translatedSequence}")
  print(f"Protein mass: {totalMass}")
