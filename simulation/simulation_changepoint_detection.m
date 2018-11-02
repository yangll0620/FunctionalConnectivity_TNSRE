function points_change  = simulation_changepoint_detection()
% detect the change points on the simulation dataset
addpath('..\')

load('.\matrixConn_Surrogate.mat'); % load matrix_Con_Surr
[points_change,diff] = changepoint_detection_cosSimilarity(matrix_Con_Surr);
plot(diff)
saveas(gcf, 'cosSimilarity.png','png')
disp(['change points are  ' num2str(points_change')])
