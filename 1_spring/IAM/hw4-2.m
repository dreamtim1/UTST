%Define a function
x = linspace(-5, 1, 31);
y = 5 .* exp(-x) .* sin(x);

% Draw a plot
figure(2);
stem(x, y, 'filled');
xlim([-5, 1]);
ylim([-100, 800]);
grid on;