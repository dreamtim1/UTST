%Define a function
x = linspace(-10, 10, 1000);
y = 2 .^ log(abs(cos(x./2 + 1))) + 3 .* cos(x./10);

% Draw a plot
figure(1);
plot(x, y);
xlim([-10, 10]);
ylim([0, 5]);
grid on;