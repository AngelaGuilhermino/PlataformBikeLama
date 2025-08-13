document.addEventListener('DOMContentLoaded', function () {
  const calendarEl = document.getElementById('calendar');
  const modalEl = new bootstrap.Modal(document.getElementById('eventModal'));
  const form = document.getElementById('eventForm');

  let currentEventId = null;
  let calendar;

  // Carrega eventos do localStorage
  function loadEvents() {
    const stored = localStorage.getItem('eventos');
    return stored ? JSON.parse(stored) : [];
  }

  // Salvar eventos no localStorage
  function saveEvents(events) {
    localStorage.setItem('eventos', JSON.stringify(events));
  }

  // Inicializa o calendário
  calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    locale: 'pt-br',
    selectable: true,
    events: loadEvents(),
    dateClick(info) {
      currentEventId = null;
      form.reset();
      document.getElementById('eventDate').value = info.dateStr;
      document.getElementById('deleteEvent').style.display = 'none';
      modalEl.show();
    },
    eventClick(info) {
      const event = info.event;
      currentEventId = event.id;
      document.getElementById('eventId').value = event.id;
      document.getElementById('eventTitle').value = event.title;
      document.getElementById('eventDate').value = event.startStr;
      document.getElementById('deleteEvent').style.display = 'inline-block';
      modalEl.show();
    },
  });

  calendar.render();

  // Salvar evento novo ou editar
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const title = document.getElementById('eventTitle').value;
    const date = document.getElementById('eventDate').value;

    let events = loadEvents();

    if (currentEventId) {
      // Edita evento existente
      events = events.map(ev => ev.id === currentEventId ? { id: ev.id, title, start: date } : ev);
      calendar.getEventById(currentEventId)?.remove();
    } else {
      // Cria novo evento
      const id = Date.now().toString();
      events.push({ id, title, start: date });
    }

    saveEvents(events);
    calendar.removeAllEvents();
    calendar.addEventSource(events);
    modalEl.hide();
  });

  // Exclui evento
  document.getElementById('deleteEvent').addEventListener('click', function () {
    if (currentEventId) {
      let events = loadEvents().filter(ev => ev.id !== currentEventId);
      saveEvents(events);
      calendar.getEventById(currentEventId)?.remove();
      modalEl.hide();
    }
  });
});
