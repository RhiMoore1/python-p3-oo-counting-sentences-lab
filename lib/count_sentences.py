#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
    
  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str) and value is not None:
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    value = self.value.replace('!', '.').replace('?', '.')
    print('Modified value:', value) 
    sentences = [sentence.strip() for sentence in value.split('.') if sentence.strip()]
    print("Sentences:", sentences)
    print("How many sentences:", len(sentences))
    count = len(sentences)
    return count

  



