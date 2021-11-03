%data -> 1.1/1.2
A = 'hello';
C = [];
C{1} = 'hello';
C{2} = 'goodbye';
C{3} = 'hola';
C{4} = 'hello hellen';
C{5} = 'helmet';
C{6} = 'hellorheaven';
C{7} = 'hillsboro';
C{8} = 'say hello';
C{9} = 'myfellow';

%Vars to store answers to 1.3
numHello_exact = length(find(strcmp(C, A)));
numHello_word = 0;

%find *word* A
numHello_word_arr = strfind(C, A);

%feeling loopy
for i = 1:length(C)
    numHello_word = numHello_word + length(find(numHello_word_arr{i}));
end

%1.4 data
D = 'goodfellow';
letters_array = []; %not even sure how to init size here but matlab really wants me to ):

%loopin'
for i = 1:length(C)
    letters_array{i} = strlength(intersect(D, C{i}));
end

%1.5 - letter locations

letters_array_positional = [];

for x = 1:length(C)
   word = C{x};
   
   similars = 0;
   
   for y = 1:length(word)
       
       if y > length(D)
           break
       end
       
       if word(y) == D(y)
           similars = similars + 1;
       end
   end
   
   letters_array_positional{x} = similars;
end