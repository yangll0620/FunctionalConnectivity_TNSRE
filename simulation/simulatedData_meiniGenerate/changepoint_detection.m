clear
addpath('..\..\')

prefix = 'sim_chaos_colpitts_p64_';
noisy_= 'conn_nt_noisy';
load([prefix 'r6_LF_' noisy_ '.mat'],'conn_nt_ciCOH','conn_nt_ciPLV')
conn_1 = conn_nt_ciCOH;
load([prefix 'r6_LF+RP_' noisy_ '.mat'],'conn_nt_ciCOH','conn_nt_ciPLV')
conn_2 = conn_nt_ciCOH;
load([prefix 'r4_3r_3inter_' noisy_ '.mat'],'conn_nt_ciCOH','conn_nt_ciPLV')
conn_3 = conn_nt_ciCOH;
% change point:
ind_str = 101;
data1 = conn_1(:,:,ind_str:end); data2 = conn_2(:,:,ind_str:end); data3 = conn_3(:,:,ind_str:end);
matrix_Con_Surr = cat(3,data1,data2,data3);
change_point1 = size(data1,3) +1;
change_point2 = change_point1 + size(data2,3);
disp(['actual change Points = ' num2str([change_point1 change_point2])])

%%
[points_change,distances] = changepoint_detection_cosSimilarity(matrix_Con_Surr);
set(gcf, 'pos',[360 200 400 200])
plot(((1:length(distances))+1),distances)
hold on
y = ylim();
% for i = 1: length(points_change)
%     x = points_change(i);
%     plot([x x],[y(1) y(2)],'--r')
% end
ylim(y)
% ylabel('Distance')
% xlabel('points')
print(gcf,'simulation_changepoint.png','-dpng','-r300');
disp(['change points are  ' num2str(points_change')])