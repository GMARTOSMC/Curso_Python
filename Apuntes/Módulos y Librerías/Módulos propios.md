
Podemos importar nuestros propios ficheros de python como módulos. Para ello importamos el nombre del fichero sin la extensión, podemos renombrarlos y podemos usar los elementos de ese módulo como hacemos en los módulos ya creamos. Ejemplo en el que importo dos módulos a partir de los ficheros ***hangman_art.py*** y ***hangman_words.py***

```python
import random, hangman_art as h_art, hangman_words as h_words
print(h_art.logo)

chosen_word = random.choice(h_words.word_list)
word_length = len(chosen_word)
```


En el fondo es igual que los módulos ya preexistentes.  En este caso logo y word_list son variables creadas en esos módulos. También podemos llamar funciones igual que en los módulos preexistentes.