import strdist.m.*;


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

d = 'goodfellow';

results = [];

for i = 1:length(C)
    results{end+1} = strdist(d, C{i});
end