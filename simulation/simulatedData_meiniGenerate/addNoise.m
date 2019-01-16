function addNoise()
% loadfile = 'sim_chaos_colpitts_p64_r6_LF+RP.mat';
% addNosie(loadfile);
% loadfile = 'sim_chaos_colpitts_p64_r6_LF.mat';
% addNosie(loadfile);
% loadfile = 'sim_chaos_colpitts_p64_r4_3r_iid.mat';
% addNosie(loadfile);

prefix = 'sim_chaos_colpitts_p64_';
addNoise_perfile([prefix 'r4_3r_3inter' '.mat']);


function addNoise_perfile(loadfile)
load(loadfile) % n_chns * n_times * n_epochs
[n_chns, n_times, n_epochs]= size(data_comp);
data_noisy = zeros(size(data_comp));
snr = 40;
for i_chn = 1: n_chns
    for i_epoch = 1:n_epochs
        in = squeeze(data_comp(i_chn, :, i_epoch));
        data_noisy(i_chn, :, i_epoch) = awgn(in,snr); 
    end
end
save(loadfile, 'data_comp','conn_nt','data_noisy');
