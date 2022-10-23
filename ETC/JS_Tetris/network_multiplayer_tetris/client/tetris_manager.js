class TetrisManager
{
	constructor(document)
	{
		this.document = document;
		this.template = this.document.getElementById('player-template');

		this.instances = [];
	}
	
	createPlayer()
	{
		const element = document
			.importNode(this.template.content, true)
			.children[0];
			
		const tetris = new Tetris(element);

		this.document.body.appendChild(tetris.element);
		this.instances.push(tetris);

		return tetris;
	}

	removePlayer(tetris)
	{
		this.document.body.removeChild(tetris.element);

        this.instances = this.instances.filter(
            (instance) => instance !== tetris
        );
	}

	sortPlayer(tetris)
	{
		tetris.forEach(tetris => {
			this.document.body.appendChild(tetris.element);
		})
	}
}
