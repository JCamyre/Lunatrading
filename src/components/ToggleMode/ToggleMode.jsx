import React from 'react';
import {ThemeConsumer} from 'styled-components';
import ToggleButton from '../ToggleButton/ToggleButton';
import '../ToggleButton/ToggleButton.css'; // prob ToggleButton deal with it's own css

export default function ToggleMode() {
    return (
        <ThemeConsumer>
            {theme => (
                <ToggleButton
                    variant='primary'
                    onClick = {(e) => 
                        theme.setTheme(theme.mode === 'dark' ? {...theme, mode: 'light' } : {...theme, mode: 'dark' })
                    }>
                Toggle Theme
                </ToggleButton>
            )}
        </ThemeConsumer>
    )
}