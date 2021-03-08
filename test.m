clear ; close all; clc


theta_t = [-2; -1; 1; 2];
X_t = [ones(5,1) reshape(1:15,5,3)/10];
y_t = ([1;0;1;0;1] >= 0.5);
lambda_t = 3;
[J grad] = cost(theta_t, X_t, y_t, lambda_t);


disp(J);
disp(grad);









%
