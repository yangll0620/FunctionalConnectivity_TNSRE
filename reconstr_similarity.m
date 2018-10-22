function recon_similarity = reconstr_similarity(A, A_base)
% ref: Mahyari and Aviyente, 2013, Two-dimensional SVD for event detection in dynamic functional brain networks
% input: A, A_base: with same dimensions

recon_similarity = nor_infinity(A-A_base)/norm_infinity(A_base);

function norm_inf = norm_infinity(A)
% calculate the infinity norm of Matrix A
norm_inf = max(sum(abs(A),2)); 