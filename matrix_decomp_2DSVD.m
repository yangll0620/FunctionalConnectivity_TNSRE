function [U, V]= matrix_decomp_2DSVD(Z,dim)
% 2DSVD along the dimension dim
% input: 3-dimentional tensor Z (m*n*t), dimension dim (default: dim = 3)
% output:
%           U, V are the eigenvectors 
%           Z_approx = U * U' * Z_i * V * V'
%       or  Z_approx_lowRank(:,:,i) = U(:,1:k) * U(:,1:k)' * Z_i * V(:,1:s) * V(:,1:s)';

if nargin < 2
    dim = 3;
end
if dim == 1
    Z = permute(Z,[2 3 1]);
end
if dim == 2
    Z = permute(Z,[1 3 2]);
end

Z_bar = squeeze(mean(Z,3)); % mean matrix

% row-row and column-column variance matrix
M = size(Z,3);
var_row_sum = 0;
var_column_sum = 0;
for i = 1:M
    Z_i = squeeze(Z(:,:,i));
    var_row_sum = var_row_sum + (Z_i - Z_bar)*(Z_i - Z_bar)';
    var_column_sum = var_column_sum + (Z_i - Z_bar)'*(Z_i - Z_bar);
    clear Z_i
end
var_row = var_row_sum/M;
var_column = var_column_sum/M;
clear var_row_sum var_column_sum

[U, LAMDA] = eig(var_row); % U: columns are the corresponding eigenvectors
[V, EPSILON] = eig(var_column);








