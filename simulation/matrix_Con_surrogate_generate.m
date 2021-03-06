function matrix_Con_Surr = matrix_Con_surrogate_generate()
% generate surrogate connectivity matrix 
% ref: 
%   Mahyari et al (2017 TBME)'A Tensor Decomposition-Based Approach for Detecting Dynamic Network States From EEG', 
% return:
%        matrix_Con_Surr : n_chns * n_chns * n_time(default: 64 * 64 * 180)

% time: 1:180, change point: 61, 121
change_point1 = 61; % 
change_point2 = 121;
n_time = 180;
n_chns = 64;

matrix_Con_Surr = zeros(n_chns, n_chns, n_time); % connectivity matrix
% weak connections across all the channels
for i_time = 1: n_time
    for i_chn = 1:n_chns
        for j_chn = i_chn + 1:n_chns
            weight = normrnd(0.1,0.02);  
            matrix_Con_Surr(i_chn, j_chn, i_time) = weight;
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight; 
            clear weight
        end
    end
end

% in time [1:60]
ind_Cluster = [1:30]; % total edges = nchoosek(30,2) = 435
for i_time = 1:change_point1-1
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.7] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight; 
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
    clear i
end
clear ind_Cluster i_time
ind_Cluster = [31:64]; % total edges = nchoosek(20,2) = 435
for i_time = 1:change_point1-1
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.7] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight; 
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
    clear i
end
clear ind_Cluster i_time
% %%%%%%%%%%% in time [1:60]

% in [61:120]
ind_Cluster = [1:15]; % total edges = nchoosek(30,2) = 435
for i_time = change_point1 : change_point2-1
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.7] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight;  
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
end
clear ind_Cluster i_time
ind_Cluster = [16:48]; % total edges = nchoosek(30,2) = 435
for i_time = change_point1 : change_point2-1
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.7] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight;  
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
end
clear ind_Cluster i_time
ind_Cluster = [49:64]; % total edges = nchoosek(30,2) = 435
for i_time = change_point1 : change_point2-1
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.7] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight;  
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
end
clear ind_Cluster i_time
% %%%%%%%%%%%%%%%%% in [61:120]

% in [121:180]
ind_Cluster = [1:44]; % total edges = nchoosek(30,2) = 435
for i_time = change_point2 : n_time
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.6] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight; 
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
end
clear ind_Cluster i_time
ind_Cluster = [45:64]; % total edges = nchoosek(30,2) = 435
for i_time = change_point2 : n_time
    for i = 1:length(ind_Cluster)
        i_chn = ind_Cluster(i);
        for j = i+1:length(ind_Cluster)
            j_chn = ind_Cluster(j);
            
            mu = rand(1)*0.4+0.3;
            weight = normrnd(mu,0.01); % mu in [0.3,0.6] 
            matrix_Con_Surr(i_chn,j_chn,i_time) = weight; 
            matrix_Con_Surr(j_chn,i_chn,i_time) = weight; 
            clear i_chn_inner mu weight j_chn
        end 
        clear i_chn j
    end
end
clear ind_Cluster i_time
% %%%%%%%%%%%%%%%%% in [121:180]

save('matrixConn_Surrogate.mat','matrix_Con_Surr')


