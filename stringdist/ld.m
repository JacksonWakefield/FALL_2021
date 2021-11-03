% http://stackoverflow.com/questions/3655612/...
% how-to-compute-similarity-between-two-sentences-syntactical-and-semantical

% compute Levenshtein distance (LD) between sentences and then 
% decide if the 2nd sentence:
% - can be ignored (INPUT1 and 2),
% - should replace the first sentence (INPUT 3), or
% - stored along with the first sentence (INPUT4).
%# As the difference is computed, a decision is made on the new event
%# (string 2) to be ignored, to replace existing event (string 1) or to be
%# stored separately. The higher the LD metric, the higher the difference
%# between two strings. Of course, lower difference indices either identical
%# or similar events. However, the higher difference indicates the new event
%# as a fresh event.

%#.........................................................................
%# Calculating the LD between two strings of events.
%#.........................................................................
L1=length(str1)+1;
L2=length(str2)+1;
L=zeros(L1,L2);   %# Initializing the new length.

g=+1;             %# just constant
m=+0;             %# match is cheaper, we seek to minimize
d=+1;             %# not-a-match is more costly.

% do BC's
L(:,1)=([0:L1-1]*g)';
L(1,:)=[0:L2-1]*g;

m4=0;             %# loop invariant
%# Calculating required edits.
for idx=2:L1;
    for idy=2:L2
        if(str1(idx-1)==str2(idy-1))
            score=m;
        else
            score=d;
        end
        m1=L(idx-1,idy-1) + score;
        m2=L(idx-1,idy) + g;
        m3=L(idx,idy-1) + g;
        L(idx,idy)=min(m1,min(m2,m3)); % only minimum edits allowed.
    end
end
%# The LD between two strings.
D=L(L1,L2);

%#....................................................................
%# Making decision on what to do with the new event (string 2).
%#...................................................................
if (D<=4)     %# Distance is so less that string 2 seems identical to string 1.
    store=str1;        %# Hence string 2 is ignored. String 1 remains stored.
elseif (D>=5 && D<=15) %# Distance is larger to be identical but not enough to
    %# make string 2 an individual event.
    store= str2;       %# String 2 is somewhat similar to string 1.
                       %# So, string 1 is replaced with string 2 and stored.
else
    %# For all other distances, string 2 is stored along with string 1.
    store={str1; str2};
end
