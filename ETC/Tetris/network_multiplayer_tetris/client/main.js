const tetrisManager = new TetrisManager(document);
const localTetris = tetrisManager.createPlayer();

const connectionManager = new ConnectionManager();
connectionManager.connect('ws://localhost:9000');

const keyListener = (event) => {
	[
		[37, 39, 40, 32],
		[65, 68, 83, 13],
	].forEach((key, index) => {
		const player = localTetris.player;
		if (event.type === 'keydown') {
			if (event.keyCode === key[0]) {
				player.move(-1);
			} else if (event.keyCode === key[1]) {
				player.move(1);
			} else if (event.keyCode === key[3]) {
				player.rotate(1);
			}
		}

		if (event.keyCode === key[2]) {
			if (event.type === 'keydown') {
				if (player.dropInterval !== player.DROP_FAST) {
					player.drop();
					player.dropInterval = player.DROP_FAST;
				}
			} else {
				player.dropInterval = player.DROP_SLOW;
			}
		}
	});
};

document.addEventListener('keydown', keyListener);
document.addEventListener('keyup', keyListener);
