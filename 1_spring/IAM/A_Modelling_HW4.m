%Define a function
t = linspace(-10, 10, 1000);
w = 2 .^ log(abs(cos(t./2 + 1))) + 3 .* cos(t./10);

% Draw a plot
figure(1);
plot(t, w);
xlim([-10, 10]);
ylim([0, 5]);
grid on;