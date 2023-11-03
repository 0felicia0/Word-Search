from funcs import *

def main():
   puzzle = input();
   words = input();

   puzzle = [puzzle[c : c + 10] for c in range(0, len(puzzle), 10)];
   words = words.split();

   print("Puzzle: \n");
   for row in puzzle:
      print(*row, sep = "");

   # first letter of each word to be found
   first_c = [word[0] for word in words]; #['U', 'C', 'G', 'S', 'C', 'C', 'V', 'T'] puzzle0

   loc = []; # list of lists of tuples [[(x, y)...], [(x, y)...], ...]

   # get locations of each c 
   for c in first_c:
      loc.append(get_locations_c(puzzle, c));

   print();

   for l in range(len(loc)):
      cur_word = words[l];
      found = False;
      for t in loc[l]:
         # starting point
         # tuple in spot 0 is row, spot 1 is col
         row = t[0];
         col = t[1];
         
         if check_all(puzzle, row, col, cur_word):
            found = True;

      if found == False:
         print("%s: word not found" % cur_word);

if __name__ == '__main__':
   main()