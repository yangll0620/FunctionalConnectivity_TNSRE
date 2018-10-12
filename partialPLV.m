function [parConnMat] = partialPLV(connMat)
% function [parConnMat] = partialPLV(connMat)
%
% connMat size: chan*chan
%
% parConnMat size: chan*chan

invConn = pinv(connMat);
autoInv = diag(invConn);
delim = autoInv * autoInv';
parConnMat = real(abs(invConn) ./ sqrt(delim));

end