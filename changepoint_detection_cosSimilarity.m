function [points_change, distances] = changepoint_detection_cosSimilarity(matrix_Con)
% detect the change points using connectivity matrix based on cosine similarity

% input:    
%           matrix_Con: connectivity matrix, n_chns * n_chns * n_times
% output:
%           points_change: a vector, the change point indices
%           distances: a vector, the differences along time

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
    distances(i_time-1,1) = sqrt(sum(similarity_cos.^2))/r; % different matrix
    clear similarity_cos
    clear U_current U_previous r M M_base
end

% %%change points are found as the values belong to the area <signlev
signlev = 0.05; % set significant level
pd = fitdist(distances, 'Lognormal');
pct = icdf(pd, signlev);    
points_change = find(distances < pct);
interval = diff(points_change);
ind_close = find(


% %% 
% n_pre = 10;
% points_change =[];
% i = n_pre + 1;
% while(i<=length(distances))
%     series_previous = distances(i-n_pre: i-1);
%     v_mean = mean(series_previous);
%     v_std = std(series_previous);
%     if(distances(i) < v_mean - 3*v_std)
%         points_change = [points_change i];
%         i = i+ n_pre;
%     end
%     i = i+1;
% end
% points_change = points_change';

