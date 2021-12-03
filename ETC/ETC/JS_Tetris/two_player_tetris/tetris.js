class Tetris
{
	constructor(element)
	{
		this.element = element;
		this.canvas = element.querySelector('canvas');
		this.context = this.canvas.getContext('2d');
		this.context.scale(20, 20);
		
		this.arena = new Arena(12, 20);
		this.player = new Player(this);

		this.colors = [
			null, '#F30D0D',
			'#F98817', '#ffff00',
			'#79F30D', '#0DF0F3',
			'#2B49FF', '#F617F9',
		];

		let lastTime = 0;
		const update = (time = 0) => {
			const deltaTime = time - lastTime;
			lastTime = time;
			this.player.update(deltaTime);
			this.draw();
			requestAnimationFrame(update);
		};
		update();
		this.updateScore(0);
	}

	draw()
	{
		this.context.fillStyle = '#000';
		this.context.fillRect(0, 0, this.canvas.width, this.canvas.height);

		this.drawMatrix(this.arena.matrix, {x: 0, y: 0});
		this.drawMatrix(this.player.matrix, this.player.pos);
	}

	drawMatrix(matrix, offset)
	{
		matrix.forEach((row, y) => {
			row.forEach((value, x) => {
				if (value !== 0) {
					this.context.fillStyle = this.colors[value];
					this.context.fillRect(x + offset.x, y + offset.y, 1, 1);
				}
			});
		});
	}

	updateScore(score)
	{
		this.element.querySelector("#score").innerText = score;
	}

}
