package com.pets.ismaeva.checkingpets;

import android.content.Intent;
import android.graphics.drawable.AnimationDrawable;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

import java.util.Timer;
import java.util.TimerTask;


public class Presentacion extends ActionBarActivity {

    ImageView logo;
    private AnimationDrawable savingAnimation;
    private static final long tiempo1 = 50;
    private static final long tiempo2 = 3000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_presentacion);

        logo=(ImageView)findViewById(R.id.imageView);

        final Animation myRotation = AnimationUtils.loadAnimation(this, R.anim.rotator);



        //creamos una serie de tareas temporizadas que simularan el progreso de la barra
        TimerTask task1 = new TimerTask() {
            @Override
            public void run() {

                logo.startAnimation(myRotation);


            }
        };


        TimerTask task2 = new TimerTask() {
            @Override
            public void run() {

                //Intent nuevo=new Intent(getBaseContext(), MainActivity.class);
               // startActivity(nuevo);

                finish();


            }
        };



        Timer timer = new Timer();

        timer.schedule(task1, tiempo1);
        timer.schedule(task2, tiempo2);



    }


    }







