function points_change  = simulation_changepoint_detection()
% detect the change points using the simulation dataset
addpath('..\')

load('.\matrixConn_Surrogate.mat'); % load matrix_Con_Surr
points_change = changepoint_detection_cosSimilarity(matrix_Con_Surr);

