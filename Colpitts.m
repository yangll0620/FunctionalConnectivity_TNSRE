function x_dot = Colpitts(t,x)
% 	 the Colpitts Attractor 
% 		use x2
% 
% 		ref: C. Carmeli, M. G. Knyazeva, G. M. Innocenti, and O. De Feo, “Assessment of EEG synchronization based on state-space analysis,” Neuroimage, vol. 25, no. 2, pp. 339–354, 2005.
% 
% 		@ parameter 
% 			C_vector: a vector representing the coupling weight between this oscillator and all the others
% 			X2: a vector representing the x2 values of all the oscillators


	k = 0.5;
    gs = 4.006 + rand(64)*(4.428 - 4.006);
	Qs = 1.342 + rand(64)*(1.483 - 1.342);
	alphas = 0.949 + rand(64) * (0.999 - 0.949);
    
    n_chns = length(x)/3;
    for i = 1:length(x)
        eval(['x' num2str(i) '= x(' num2str(i) ');'])
    end
    
	X2 = x(2:3:end);
    C_matrix = zeros(n_chns, n_chns);
    C_matrix(2,3) = 1 + rand(1) * (3-1); C_matrix(3,2) = C_matrix(2,3);
    C_matrix(2,4) = 1 + rand(1) * (3-1); C_matrix(4,2) = C_matrix(2,4);
    C_matrix(3,4) = 1 + rand(1) * (3-1); C_matrix(4,3) = C_matrix(3,4);
    C_matrix(5,6) = 1 + rand(1) * (3-1); C_matrix(6,5) = C_matrix(5,6);
    C_matrix(5,7) = 1 + rand(1) * (3-1); C_matrix(7,5) = C_matrix(5,7);
    C_matrix(6,7) = 1 + rand(1) * (3-1); C_matrix(7,6) = C_matrix(6,7);
    C_matrix(4,7) = 1 + rand(1) * (3-1); C_matrix(7,4) = C_matrix(4,7);
    
    
    i_chn = 1;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);  
	x1_dot = g/(Q*(1-k)) * (alpha*(exp(-x2) -1) + x3);
	x2_dot = g/(Q*k)*((1 - alpha) *(exp(-x2) - 1) + x3) + sum(C_vector .*(X2 - x2));
	x3_dot = -Q*k*(1-k)/g * (x1 + x2) - 1/Q * x3;
    
    i_chn = 2;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
	x4_dot = g/(Q*(1-k)) * (alpha*(exp(-x5) -1) + x6);
	x5_dot = g/(Q*k)*((1 - alpha) *(exp(-x5) - 1) + x6) + sum(C_vector .*(X2 - x5));
	x6_dot = -Q*k*(1-k)/g * (x4 + x5) - 1/Q * x6;
    
    i_chn = 3;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
	x7_dot = g/(Q*(1-k)) * (alpha*(exp(-x8) -1) + x9);
	x8_dot = g/(Q*k)*((1 - alpha) *(exp(-x8) - 1) + x9) + sum(C_vector .*(X2 - x8));
	x9_dot = -Q*k*(1-k)/g * (x7 + x8) - 1/Q * x9;
    
    i_chn = 4;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
	x10_dot = g/(Q*(1-k)) * (alpha*(exp(-x11) -1) + x12);
	x11_dot = g/(Q*k)*((1 - alpha) *(exp(-x11) - 1) + x12) + sum(C_vector .*(X2 - x11));
	x12_dot = -Q*k*(1-k)/g * (x10 + x11) - 1/Q * x12;
    
    i_chn = 5;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
	x13_dot = g/(Q*(1-k)) * (alpha*(exp(-x14) -1) + x15);
	x14_dot = g/(Q*k)*((1 - alpha) *(exp(-x14) - 1) + x15) + sum(C_vector .*(X2 - x14));
	x15_dot = -Q*k*(1-k)/g * (x13 + x14) - 1/Q * x15;
    
    i_chn = 6;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
    x16_dot = g/(Q*(1-k)) * (alpha*(exp(-x17) -1) + x18);
	x17_dot = g/(Q*k)*((1 - alpha) *(exp(-x17) - 1) + x18) + sum(C_vector .*(X2 - x17));
	x18_dot = -Q*k*(1-k)/g * (x16 + x17) - 1/Q * x18;
    
    i_chn = 7;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
    x19_dot = g/(Q*(1-k)) * (alpha*(exp(-x20) -1) + x21);
	x20_dot = g/(Q*k)*((1 - alpha) *(exp(-x20) - 1) + x21) + sum(C_vector .*(X2 - x20));
	x21_dot = -Q*k*(1-k)/g * (x19 + x20) - 1/Q * x21;
    
    i_chn = 8;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
    x22_dot = g/(Q*(1-k)) * (alpha*(exp(-x23) -1) + x24);
	x23_dot = g/(Q*k)*((1 - alpha) *(exp(-x23) - 1) + x24) + sum(C_vector .*(X2 - x23));
	x24_dot = -Q*k*(1-k)/g * (x22 + x23) - 1/Q * x24;
    
    i_chn = 9;
    C_vector = C_matrix(:, i_chn);
	g = gs(i_chn); Q = Qs(i_chn); alpha = alphas(i_chn);
    x25_dot = g/(Q*(1-k)) * (alpha*(exp(-x26) -1) + x27);
	x26_dot = g/(Q*k)*((1 - alpha) *(exp(-x26) - 1) + x27) + sum(C_vector .*(X2 - x26));
	x27_dot = -Q*k*(1-k)/g * (x25 + x26) - 1/Q * x27;

    x_dot = [x1_dot; x2_dot; x3_dot; x4_dot; x5_dot; x6_dot; x7_dot; x8_dot; x9_dot; ... 
        x10_dot; x11_dot; x12_dot; x13_dot; x14_dot; x15_dot; x16_dot; x17_dot; x18_dot; ... 
        x19_dot; x20_dot; x21_dot; x22_dot; x23_dot; x24_dot; x25_dot; x26_dot; x27_dot];
    

