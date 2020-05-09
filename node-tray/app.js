const SysTray = require('systray').default;
const { execSync } = require('child_process');
const configs = require('../configs.json');
const images = require('./images');

function executeCommand(command) {
    console.log(`< ${command}`);
    const out = execSync(command).toString('utf8');
    console.log(`> ${out}`);
}

const items = [
    {
        title: 'on',
        enabled: true,
        action: () => {
            executeCommand('light on');
        }
    },
    {
        title: 'off',
        enabled: true,
        action: () => {
            executeCommand('light off');
        }
    },
];

Object.keys(configs.scenes).forEach(s => {
    items.push({
        title: `scene ${s}`,
        enabled: true,
        action: () => {
            executeCommand(`light scene ${s}`);
        }
    });
});

const systray = new SysTray({
    menu: {
        title: 'Room Light',
        icon: images.icon,
        items
    }
});

systray.onClick(action => {
    items[action.seq_id].action();
});