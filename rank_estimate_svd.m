function [k, U_base, V_base, E_weight,M_approx] = rank_estimate_svd(M)
% estimate the optimal value of the low-rank approximation of M using SVD
% input: matrix M
% output: 
%           k: the optimal rank 
%           U_base, V_base: the corresponding bases
%           E: the corresponding coefficient matrix
%           M_approx: the corresponding low-rank approximation (M_approx = U_base * E_weight * V_base')
[U,S,V] = svd(M);
for k = 1:size(M,1)
    M_est = U(:,1:k) * S(1:k,1:k) * V(:,1:k)';% M_est = U * S * V'
    % Frobenius Norm
    error(k) = norm(M-M_est,'fro');
    clear M_est
end
err_initial = norm(M,'fro');
err_decrease = 0.05;% stop at the 5% of the initial error
k = find(error>err_initial * err_decrease,1,'last');
M_approx = U(:,1:k) * S(1:k,1:k) * V(:,1:k)';

U_base = U(:,1:k);
V_base = V(:,1:k);
E_weight =  S(1:k,1:k);