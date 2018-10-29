function similarity_cos = similarity_cosine(v1,v2)
% calulate the cosine similarity of two vectors
% input: two vectors v1 and v2
% output: 
%           similarity_cos: a scalar 
similarity_cos = abs(sum(v1.*v2)/(sqrt(sum(v1.*v1))*sqrt(sum(v2.*v2))));