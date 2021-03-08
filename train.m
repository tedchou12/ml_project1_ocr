clear ; close all; clc

content1 = load('training/matrix/1.txt');
content2 = load('training/matrix/2.txt');
content3 = load('training/matrix/3.txt');
content4 = load('training/matrix/4.txt');
content5 = load('training/matrix/5.txt');
content6 = load('training/matrix/6.txt');
content7 = load('training/matrix/7.txt');
content8 = load('training/matrix/8.txt');
content9 = load('training/matrix/9.txt');
content10 = load('training/matrix/10.txt');

% training inputs, X
X = [content1; content2; content3; content4; content5; content6; content7; content8; content9; content10];
% training labels, y
y = [ones(size(content1)(1), 1) * 1; ones(size(content2)(1), 1) * 2; ones(size(content3)(1), 1) * 3; ones(size(content4)(1), 1) * 4; ones(size(content5)(1), 1) * 5; ...
    ones(size(content6)(1), 1) * 6; ones(size(content7)(1), 1) * 7; ones(size(content8)(1), 1) * 8; ones(size(content9)(1), 1) * 9; ones(size(content10)(1), 1) * 10];

% training size
m = size(X, 1);

% example for y = 0
% label = 0;
% y0 = y;
% y0(y0 == label) = 100;
% y0(y0 != 100) = 101;
% y0(y0 == 100) = 0;
% y0(y0 == 101) = 1;
% Theta0 = zeros(size(X)(2) + 1, 1);


% lambda
lambda = 0;

% calculate cost
% [J grad] = cost(Theta0, X, y0, lambda);
% n = size(X, 2);
% initial_theta = zeros(n + 1, 1);

n = size(X, 2);

X = [ones(m, 1) X];
% options = optimset('GradObj', 'on', 'MaxIter', 100);
% disp('^#');
% disp(size(X));
% disp(size((y0)));
% disp(size(lambda));
% disp(size(Theta0));
% disp(size(options));
% disp('$#');
% Theta0_f = fmincg(@(t)(cost(t, X, y0, lambda)), Theta0, options);
num_labels = 10;

Theta_f = zeros(num_labels, n + 1);

% disp(J);
% disp(size(Theta0_f));

for iter = 1:num_labels
  initial_theta = zeros(n + 1, 1);
  options = optimset('GradObj', 'on', 'MaxIter', 200);
  Theta_i = fmincg(@(t)(cost(t, X, (y == iter), lambda)), initial_theta, options);
  Theta_f(iter, :) = Theta_i;
end


fid = fopen('theta.txt', 'w+');
for i=1:size(Theta_f, 1)
    fprintf(fid, '%f ', Theta_f(i,:));
    fprintf(fid, '\n');
end
fclose(fid);

% disp(size(Theta_f));











%
