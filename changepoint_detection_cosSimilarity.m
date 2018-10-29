function [points_change, diff] = changepoint_detection_cosSimilarity(matrix_Con)
% detect the change points using connectivity matrix based on cosine similarity

% input:    
%           matrix_Con: connectivity matrix, n_chns * n_chns * n_times
% output:
%           points_change: a vector, the change point indices
%           diff: a vector, the differences along time

% low-rank approximation using SVD for each time i, extract the 
for i_time = 1:size(matrix_Con,3)
    M = squeeze(matrix_Con(:,:,i_time)); % M is connectivity matrix,
    [~, Us{i_time}, Vs{i_time}, ~,~] = rank_estimate_svd(M); % k is the same for the row and column
end

% calcuate different matrix based on cosine similarity
for i_time = 2: length(Us)
    U_current = Us{i_time}; U_previous = Us{i_time-1};
    r = min(size(U_current,2),size(U_previous,2));
    U = U_current(:,1:r);U_base = U_previous(:,1:r);
    for i_comp = 1: r
        v1 = U(:,i_comp); v2 = U_previous(:,i_comp);
        similarity_cos(i_comp) = similarity_cosine(v1,v2); % cosine similarity
        clear v1 v2
    end
    diff(i_time-1,1) = sqrt(sum(similarity_cos.^2))/r; % different matrix
    clear similarity_cos
    clear U_current U_previous r M M_base
end

signlev = 0.05;
pd = fitdist(diff, 'Lognormal');
pct = icdf(pd, signlev);    
points_change = find(diff < pct);