function Z_approx_lowRank = matrix_approx_lowRank(Z, k, s)
% low rank marix approximation along dimension 3
% low-rank approximation of a set of matrices Z_1, Z_2,...Z_M
% input: 
%       3-dimentional tensor Z (m*n*t)
%       k, s: the low rank values along the matrix 
%       dim: dimension (default: dim = 3)
% 
% output:
%           Z_approx_lowRank : low rank approximation matrix

[U, V]= matrix_decomp_2DSVD(Z,3);

U_k = U(:,1:k); % select the first k vectors
V_s = U(:,1:s); % select the first k vectors

for i = 1:M
    Z_i = squeeze(Z(:,:,i));
    Z_approx_lowRank(:,:,i) = U_k * U_k' * Z_i * V_s * V_s';
    clear Z_i
end